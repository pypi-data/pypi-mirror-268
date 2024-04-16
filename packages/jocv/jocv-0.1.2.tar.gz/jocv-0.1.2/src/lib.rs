mod colmap_io;
mod image;
mod camera_models;
mod point3d;
mod track;
mod types;
mod utils;



use glam::DVec3;
use pyo3::types::PyList;
use camera_models::Camera;
use image::Image;
use point3d::Point3D;
//use utils;
use pyo3::prelude::*;
use std::collections::HashMap;

#[pyfunction]
fn read_cameras_bin(path: &str) -> PyResult<Vec<Camera>>{
    let cams = colmap_io::read_cameras_bin(path).unwrap();
    return Ok(cams);
}

#[pyfunction]
fn read_images_bin(path: &str) -> PyResult<Vec<Image>>{
    let images = colmap_io::read_images_bin(path).unwrap();
    return Ok(images);
}

#[pyfunction]
fn read_points3D_bin(path: &str) -> PyResult<Vec<Point3D>>{
    let points3D = colmap_io::read_points3D_bin(path).unwrap();
    return Ok(points3D);
}

#[pyfunction]
fn compute_overlaps(points3D: Vec<Point3D>, num_images: usize) -> PyResult<Vec<HashMap<u32, u32>>>{
    let overlaps = utils::compute_overlaps(points3D, num_images + 1);
    return Ok(overlaps);
}

/// A Python module implemented in Rust.
#[pymodule]
fn jcv(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Camera>()?;
    m.add_class::<Image>()?;
    m.add_class::<Point3D>()?;
    m.add_function(wrap_pyfunction!(read_images_bin, m)?)?;
    m.add_function(wrap_pyfunction!(read_cameras_bin, m)?)?;
    m.add_function(wrap_pyfunction!(read_points3D_bin, m)?)?;
    m.add_function(wrap_pyfunction!(compute_overlaps, m)?)?;
    Ok(())
}
