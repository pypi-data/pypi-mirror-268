#![allow(non_snake_case)]
//use ndarray::{array, Array1, Array2};
mod camera_models;
mod point3d;
mod types;
mod track;
mod image;
mod colmap_io;
mod utils;

use colmap_io::{read_points3D_bin, read_images_bin, read_cameras_bin};
use utils::compute_overlaps;

fn main() {
    let cameras = read_cameras_bin("data/sparse/cameras.bin");
    let points = read_points3D_bin("data/sparse/points3D.bin").unwrap();
    let images = read_images_bin("data/sparse/images.bin").unwrap();
    let res = compute_overlaps(points, images.len()+1); // TODO: why would no +1 work in COLMAP
}