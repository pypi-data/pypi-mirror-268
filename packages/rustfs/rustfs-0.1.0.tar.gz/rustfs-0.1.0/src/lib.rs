use futures::StreamExt;

use object_store::multipart::MultiPartStore;
use object_store::{aws::AmazonS3Builder, path::Path, ObjectStore, MultipartId};

use pyo3::prelude::*;
use pyo3::types::PyDict;
use pyo3::PyErr;
use pyo3::types::{PyBytes};
use std::io::{Read, SeekFrom};
use std::{cmp, fs, sync::Arc};
use std::collections::HashMap;
use pyo3::exceptions::{PyValueError};

use tokio::io::{AsyncReadExt, AsyncSeekExt, AsyncWriteExt, AsyncWrite};

pub trait MultiPartObjectStore: ObjectStore + MultiPartStore {}

impl<T: ObjectStore + MultiPartStore> MultiPartObjectStore for T {}

type DynMultiPartObjectStore = dyn MultiPartObjectStore;

fn get_kwarg_string(kwargs: &PyDict, key: &str) -> Option<String> {
    kwargs.get_item(key).map(|value| value.extract().unwrap())
}

fn get_kwarg_bool(kwargs: &PyDict, key: &str) -> Option<bool> {
    kwargs.get_item(key).map(|value| value.extract().unwrap())
}

#[pyclass]
struct RustS3FileSystem {
    file_system: Option<RustFileSystem>,
    bucket: Option<String>,
    access_key_id: Option<String>,
    secret_access_key: Option<String>,
    region: Option<String>,
    endpoint: Option<String>,
    allow_http: Option<bool>,
    sep: String,
}

impl RustS3FileSystem {
    fn set_store(&mut self, refresh: Option<bool>) {
        let refresh = refresh.unwrap_or(false);
        if self.file_system.is_some() && !refresh {
            return;
        }
        let s3 = self.build_store();
        self.file_system = Option::from(RustFileSystem::new(s3));
    }

    fn build_store(&self) -> Arc<DynMultiPartObjectStore> {
        let s3 = AmazonS3Builder::from_env();
        let s3 = match &self.bucket {
            Some(bucket) => s3.with_bucket_name(bucket),
            None => s3,
        };
        let s3 = match &self.access_key_id {
            Some(access_key_id) => s3.with_access_key_id(access_key_id),
            None => s3,
        };
        let s3 = match &self.secret_access_key {
            Some(secret_access_key) => s3.with_secret_access_key(secret_access_key),
            None => s3,
        };
        let s3 = match &self.region {
            Some(region) => s3.with_region(region),
            None => s3.with_region("us-east-2"),
        };
        let s3 = match &self.endpoint {
            Some(endpoint) => s3.with_endpoint(endpoint),
            None => s3,
        };
        let s3 = match &self.allow_http {
            Some(allow_http) => s3.with_allow_http(*allow_http),
            None => s3,
        };
        let s3 = s3.build().expect("error creating s3");
        Arc::new(s3)
    }
}

#[pymethods]
impl RustS3FileSystem {
    #[new]
    #[pyo3(signature = (* * kwargs))]
    pub fn new(kwargs: Option<&PyDict>) -> Self {
        // let store = new_s3_store();
        match kwargs {
            Some(kwargs) => {
                let bucket = get_kwarg_string(kwargs, "bucket");
                let access_key_id = get_kwarg_string(kwargs, "access_key_id");
                let secret_access_key = get_kwarg_string(kwargs, "secret_access_key");
                let region = get_kwarg_string(kwargs, "region");
                let endpoint = get_kwarg_string(kwargs, "endpoint");
                let allow_http = get_kwarg_bool(kwargs, "allow_http");
                RustS3FileSystem {
                    file_system: None,
                    bucket,
                    access_key_id,
                    secret_access_key,
                    region,
                    endpoint,
                    allow_http,
                    sep: "/".to_string(),
                }
            }
            None => RustS3FileSystem {
                file_system: None,
                bucket: None,
                access_key_id: None,
                secret_access_key: None,
                region: None,
                endpoint: None,
                allow_http: None,
                sep: "/".to_string(),
            },
        }
    }

    #[getter]
    fn sep(&self) -> PyResult<String> {
        Ok(self.sep.clone())
    }

    #[pyo3(signature = (path, **_py_kwargs))]
    fn is_dir(&mut self, path: String, _py_kwargs: Option<&PyDict>) -> bool {
        let url = url::Url::parse(&path).unwrap();
        let (bucket, path) = (url.host_str().unwrap_or_default(), url.path());
        if bucket != String::default() {
            self.bucket = Option::from(bucket.to_string());
        }
        self.set_store(Some(false));
        match &self.file_system {
            Some(fs) => fs.is_dir(path.to_string(), _py_kwargs),
            None => false,
        }
    }

    #[pyo3(signature = (path, **_py_kwargs))]
    fn ls(&mut self, path: String, _py_kwargs: Option<&PyDict>) -> PyResult<Vec<String>> {
        let url = url::Url::parse(&path).unwrap();
        let (bucket, path) = (url.host_str().unwrap_or_default(), url.path());
        if bucket != String::default() {
            self.bucket = Option::from(bucket.to_string());
        }
        self.set_store(Some(false));
        match &self.file_system {
            Some(fs) => fs.ls(path.to_string(), _py_kwargs),
            None => Ok(vec![]),
        }
    }

    #[pyo3(signature = (key, value, * * _py_kwargs))]
    fn put_content(
        &self,
        key: String,
        value: Vec<u8>,
        _py_kwargs: Option<&PyDict>,
    ) -> PyResult<()> {
        match &self.file_system {
            Some(fs) => fs.put_content(key, value, _py_kwargs),
            None => Ok(()),
        }
    }

    #[pyo3(signature = (key, * * _py_kwargs))]
    fn get_content(&self, key: String, _py_kwargs: Option<&PyDict>) -> PyResult<Vec<u8>> {
        match &self.file_system {
            Some(fs) => fs.get_content(key, _py_kwargs),
            None => Ok(vec![]),
        }
    }

    #[pyo3(signature = (lpath, rpath, recursive = false, * * _py_kwargs))]
    fn put(
        &mut self,
        lpath: String,
        rpath: String,
        recursive: bool,
        _py_kwargs: Option<&PyDict>,
    ) -> PyResult<()> {
        let url = url::Url::parse(&rpath).unwrap();
        let (bucket, path) = (url.host_str().unwrap_or_default(), url.path());
        if bucket != String::default() {
            self.bucket = Option::from(bucket.to_string());
        }
        self.set_store(Some(false));
        match &self.file_system {
            Some(fs) => fs.put(lpath, path.to_string(), recursive, _py_kwargs),
            None => Ok(()),
        }
    }

    #[pyo3(signature = (path, mode, * * _py_kwargs))]
    fn open(
        &mut self,
        path: String,
        mode: String,
        _py_kwargs: Option<&PyDict>,
    ) -> PyResult<FileHandleForWrite> {
        let url = url::Url::parse(&path).unwrap();
        let (bucket, path) = (url.host_str().unwrap_or_default(), url.path());
        if bucket != String::default() {
            self.bucket = Option::from(bucket.to_string());
        }
        self.set_store(Some(false));
        match &self.file_system {
            Some(fs) => fs.open(path.to_string(), mode, _py_kwargs),
            None => Err(PyErr::new::<PyValueError, _>("no file system")),
        }
    }

    #[pyo3(signature = (rpath, lpath, recursive = false, * * _py_kwargs))]
    fn get(
        &mut self,
        rpath: String,
        lpath: String,
        recursive: bool,
        _py_kwargs: Option<&PyDict>,
    ) -> PyResult<()> {
        let url = url::Url::parse(&rpath).unwrap();
        let (bucket, path) = (url.host_str().unwrap_or_default(), url.path());
        if bucket != String::default() {
            self.bucket = Option::from(bucket.to_string());
        }
        self.set_store(Some(false));
        match &self.file_system {
            Some(fs) => fs.get(lpath, path.to_string(), recursive, _py_kwargs),
            None => Ok(()),
        }
    }

    #[staticmethod]
    fn _get_kwargs_from_urls(py: Python, urlpath: String) -> PyResult<&PyDict> {
        let dict = PyDict::new(py);
        Ok(dict.into())
    }

}

pub struct RustFileSystem {
    store: Arc<DynMultiPartObjectStore>,
    rt: tokio::runtime::Runtime,
}

#[pyclass]
pub struct FileHandleForWrite {
    path: Path,
    store: Arc<DynMultiPartObjectStore>,
    rt: tokio::runtime::Runtime,
    multipart_id: MultipartId,
    writer: Box<dyn AsyncWrite + Unpin + Send>,
}
/*  python BufferedWriter
    def close(self, *args, **kwargs): # real signature unknown
    def detach(self, *args, **kwargs): # real signature unknown
    def fileno(self, *args, **kwargs): # real signature unknown
    def flush(self, *args, **kwargs): # real signature unknown
    def isatty(self, *args, **kwargs): # real signature unknown
    def seek(self, *args, **kwargs): # real signature unknown
    def tell(self, *args, **kwargs): # real signature unknown
    def truncate(self, *args, **kwargs): # real signature unknown
 */

impl FileHandleForWrite {
    pub fn new(path: Path, store: Arc<DynMultiPartObjectStore>, multipart_id: MultipartId, writer: Box<dyn AsyncWrite + Unpin + Send>) -> Self {
        Self {
            path,
            store,
            rt: tokio::runtime::Runtime::new().unwrap(),
            multipart_id,
            writer,
        }
    }
}

#[pymethods]
impl FileHandleForWrite {

    pub fn seekable(&self) -> PyResult<bool> {
        Ok(false)
    }

    pub fn writable(&self) -> PyResult<bool> {
        Ok(false)
    }

    /// Python signature is
    /// ```python
    /// def write(self, s: AnyStr) -> int:
    /// ```
    pub fn write(&mut self, data: &PyBytes) -> PyResult<i64> {
        self.rt.block_on(async {  // why don't we need move
            let result = self.writer.write_all(data.as_bytes()).await;
            match result {
                Ok(_) => Ok(data.as_bytes().len() as i64),
                Err(err) => {
                    let abort = ObjectStore::abort_multipart(&*self.store, &self.path, &self.multipart_id).await;
                    match abort {
                        Ok(_) => Err(PyErr::new::<PyValueError, _>("hi")),
                        Err(abort_err) => Err(PyErr::new::<PyValueError, _>(abort_err.to_string() + err.to_string().as_str())),
                    }
                }
            }
        })
    }

    pub fn close(&mut self) -> PyResult<()> {
        println!("in close");
        self.rt.block_on(async {
            self.writer.flush().await.unwrap();
            self.writer.shutdown().await.unwrap();
            Ok(())
        })
    }
}

impl RustFileSystem {
    pub fn new(store: Arc<DynMultiPartObjectStore>) -> Self {
        RustFileSystem {
            store,
            rt: tokio::runtime::Runtime::new().unwrap(),
        }
    }


    /*
        def open(self, path, mode="rb",
            block_size=None, cache_options=None, compression=None, **kwargs,
        ):
     */
    fn open(&self, path: String, mode_t: String, _py_kwargs: Option<&PyDict>,
    ) -> PyResult<FileHandleForWrite> {
        let path = Path::from(path);
        if mode_t != "wb" {
            return Err(PyErr::new::<PyValueError, _>("only wb"));
        }
        self.rt.block_on(async {
            let (multipart_id, writer) = self.store.put_multipart(&path).await.unwrap();
            Ok(FileHandleForWrite::new(path, self.store.clone(), multipart_id, writer))
        })
    }

    fn is_dir(&self, path: String, _py_kwargs: Option<&PyDict>) -> bool {
        let path = Path::from(path);
        let list = self.rt.block_on(async {
            let list = self.store.list(Some(&path));
            let paths: Vec<String> = list
                .filter_map(|item| async {
                    match item {
                        Ok(item) => Some(item.location.to_string()),
                        Err(_) => None,
                    }
                })
                .collect()
                .await;
            paths
        });
        list.len() > 0
    }

    fn ls(&self, path: String, _py_kwargs: Option<&PyDict>) -> PyResult<Vec<String>> {
        let path = Path::from(path);
        let list = self.rt.block_on(async {
            let list = self.store.list(Some(&path));
            let paths: Vec<String> = list
                .filter_map(|item| async {
                    match item {
                        Ok(item) => Some(item.location.to_string()),
                        Err(_) => None,
                    }
                })
                .collect()
                .await;
            paths
        });
        Ok(list)
    }

    // put memory bytes to s3
    fn put_content(
        &self,
        key: String,
        value: Vec<u8>,
        _py_kwargs: Option<&PyDict>,
    ) -> PyResult<()> {
        let path = Path::from(key);
        self.rt.block_on(async {
            self.store.put(&path, value.into()).await.unwrap();
        });
        Ok(())
    }

    // get s3 bytes to memory
    fn get_content(&self, key: String, _py_kwargs: Option<&PyDict>) -> PyResult<Vec<u8>> {
        let path = Path::from(key);
        let bytes = self
            .rt
            .block_on(async { self.store.get(&path).await.unwrap().bytes().await.unwrap() });
        Ok(bytes.to_vec())
    }

    #[allow(dead_code)]
    fn put_file(&self, lpath: String, rpath: String, _py_kwargs: Option<&PyDict>) -> PyResult<()> {
        println!("rustfs put_file: {} -> {}", lpath, rpath);
        let file_content = fs::read(lpath).unwrap();
        let path = Path::from(rpath);
        self.rt.block_on(async {
            self.store.put(&path, file_content.into()).await.unwrap();
        });
        Ok(())
    }

    async fn put_file_optimized(
        &self,
        lpath: String,
        rpath: String,
        _py_kwargs: Option<&PyDict>,
    ) -> PyResult<()> {
        println!("rustfs put_file_optimized: {} -> {}", lpath, rpath);
        // TODO: Should we do the multipart upload by ourselves?
        let key = Path::from(rpath);
        let file_size = fs::metadata(&lpath).unwrap().len();

        // if the file is less than 100MB, use the single-part upload
        if file_size < cmp::min(5 * 2u64.pow(30), 1024 * 1024 * 100) {
            let file_content = fs::read(lpath).unwrap();
            self.store.put(&key, file_content.into()).await.unwrap();
        } else {
            const CHUNK_SIZE: u64 = 1024 * 1024 * 50;
            let mut chunk_count = (file_size / CHUNK_SIZE) + 1;
            let mut size_of_last_chunk = file_size % CHUNK_SIZE;
            if size_of_last_chunk == 0 {
                size_of_last_chunk = CHUNK_SIZE;
                chunk_count -= 1;
            }
            let upload_id = self.store.create_multipart(&key).await.unwrap();
            let upload_futures: Vec<_> = (0..chunk_count)
                .map(|chunk_index| {
                    let key = &key;
                    let lpath = &lpath;
                    let upload_id = &upload_id;
                    async move {
                        let this_chunk = if chunk_count - 1 == chunk_index {
                            size_of_last_chunk
                        } else {
                            CHUNK_SIZE
                        };
                        let start_byte = chunk_index * CHUNK_SIZE;
                        let mut file = tokio::fs::OpenOptions::new()
                            .read(true)
                            .open(&lpath)
                            .await
                            .expect("Unable to open file");
                        file.seek(SeekFrom::Start(start_byte))
                            .await
                            .expect("Failed to seek in file");
                        let mut buffer = vec![0; this_chunk as usize];
                        file.read_exact(&mut buffer)
                            .await
                            .expect("Failed to read chunk from file");
                        self.store
                            .put_part(key, upload_id, chunk_index as usize, buffer.into())
                            .await
                            .expect("Failed to upload part")
                    }
                })
                .collect();

            // create a buffered stream that will execute up to 8 futures in parallel
            let stream = futures::stream::iter(upload_futures).buffered(8);
            // wait for all futures to complete
            let parts = stream.collect::<Vec<_>>().await;
            self.store
                .complete_multipart(&key, &upload_id, parts)
                .await
                .unwrap();
        }
        Ok(())
    }

    /// Copy file(s) from local to the blob store.
    ///
    /// Copies a specific file or tree of files (if recursive=True). If rpath
    /// ends with a "/", it will be assumed to be a directory, and target files
    /// will go within.
    ///
    fn put(
        &self,
        lpath: String,
        rpath: String,
        _recursive: bool,
        _py_kwargs: Option<&PyDict>,
    ) -> PyResult<()> {
        if _recursive {
            let paths = fs::read_dir(lpath).unwrap();
            let mut lpaths: Vec<String> = vec![];
            for path in paths {
                let path = path.unwrap().path();
                let path = path.to_str().unwrap().to_string();
                lpaths.push(path);
            }
            for lpath in lpaths {
                let file_name = lpath.rsplit('/').next().unwrap_or("");
                let rpath = format!("{}/{}", rpath.trim_end_matches('/'), file_name);
                self.rt.block_on(async {
                    self.put_file_optimized(lpath, rpath, _py_kwargs)
                        .await
                        .unwrap();
                });
            }
        } else {
            self.rt.block_on(async {
                self.put_file_optimized(lpath, rpath, _py_kwargs)
                    .await
                    .unwrap();
            });
        }
        Ok(())
    }

    #[allow(dead_code)]
    fn get_file(&self, lpath: String, rpath: String, _py_kwargs: Option<&PyDict>) -> PyResult<()> {
        println!("rustfs get_file: {} -> {}", rpath, lpath);
        let path = Path::from(rpath);
        self.rt.block_on(async {
            let downloaded_bytes = self.store.get(&path).await.unwrap().bytes().await.unwrap();
            let mut file = tokio::fs::File::create(lpath).await.unwrap();
            file.write_all(&downloaded_bytes).await.unwrap();
        });
        Ok(())
    }

    async fn get_file_optimized(
        &self,
        lpath: String,
        rpath: String,
        _py_kwargs: Option<&PyDict>,
    ) -> PyResult<()> {
        println!("rustfs get_file_optimized: {} -> {}", rpath, lpath);
        let key = Path::from(rpath);
        // delete the file if it exists
        let _ = fs::remove_file(&lpath);
        let file_size = self.store.head(&key).await.unwrap().size;
        const CHUNK_SIZE: usize = 1024 * 1024 * 50;
        let mut chunk_count = file_size / CHUNK_SIZE;
        if file_size % CHUNK_SIZE > 0 {
            chunk_count += 1;
        }
        let download_futures: Vec<_> = (0..chunk_count)
            .map(|chunk_index| {
                let key = &key;
                let lpath = &lpath;
                async move {
                    let start_byte = chunk_index * CHUNK_SIZE;
                    let end_byte = std::cmp::min(start_byte + CHUNK_SIZE, file_size);
                    let downloaded_bytes = self
                        .store
                        .get_range(
                            key,
                            std::ops::Range {
                                start: start_byte,
                                end: end_byte,
                            },
                        )
                        .await
                        .unwrap();
                    // Open the file and seek to the appropriate position
                    let mut file = tokio::fs::OpenOptions::new()
                        .write(true)
                        .create(true)
                        .truncate(false)
                        .open(&lpath)
                        .await
                        .expect("Unable to open file");
                    file.seek(SeekFrom::Start(start_byte as u64))
                        .await
                        .expect("Failed to seek in file");
                    file.write_all(&downloaded_bytes)
                        .await
                        .expect("Failed to write chunk to file");
                }
            })
            .collect();
        // create a buffered stream that will execute up to 4 futures in parallel
        let stream = futures::stream::iter(download_futures).buffer_unordered(8);
        // wait for all futures to complete
        stream.collect::<Vec<_>>().await;
        Ok(())
    }

    fn get(
        &self,
        lpath: String,
        rpath: String,
        _recursive: bool,
        _py_kwargs: Option<&PyDict>,
    ) -> PyResult<()> {
        if _recursive {
            let rpaths = self.ls(rpath, _py_kwargs).unwrap();
            for rpath in rpaths {
                let file_name = rpath.rsplit('/').next().unwrap_or("");
                if file_name == rpath {
                    continue;
                }
                let lpath = format!("{}/{}", lpath.trim_end_matches('/'), file_name);
                self.rt.block_on(async {
                    self.get_file_optimized(lpath, rpath, _py_kwargs)
                        .await
                        .unwrap();
                });
            }
        } else {
            // if lpath ends with a "/", append rpath's file name to it
            let lpath = if lpath.ends_with('/') {
                format!("{}{}", lpath, rpath.rsplit('/').next().unwrap_or(""))
            } else {
                lpath
            };
            self.rt.block_on(async {
                self.get_file_optimized(lpath, rpath, _py_kwargs)
                    .await
                    .unwrap();
            });
        }
        Ok(())
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn rustfs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<RustS3FileSystem>()?;
    Ok(())
}
