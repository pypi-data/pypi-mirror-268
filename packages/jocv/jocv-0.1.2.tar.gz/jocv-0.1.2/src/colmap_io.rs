use std::fs::File;
use std::io::{self, Read};
use std::mem::size_of;

use glam::{DQuat, DVec2, DVec3};

use crate::types::{image_t, camera_t, point2D_t, point3D_t, Color};
use crate::camera_models::{CameraModelId, Camera, get_num_params};
use crate::point3d::{Point3D};
use crate::track::{TrackElement};
use crate::image::Image;


// Would like to use this, but don't understand the errors here.
//use num_traits::ops::bytes::{FromBytes};
//fn read_type<T: FromBytes>(buffer: Vec<u8>, idx: usize) -> T{
//    let offset = size_of::<T>();
//    let bytes = buffer[idx..idx+offset];
//    return T::from_le_bytes(bytes.try_into().unwrap());
//}

pub fn read_cameras_bin(path: &str)-> io::Result<Vec<Camera>>{
    // Open the file in read-only mode
    let mut file: File = File::open(path)?;

    // Read the contents of the file into a buffer
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer)?;
    // Do something with the contents of the buffer
    println!("Read {} bytes from the file", buffer.len());
    let mut idx: usize = 0;
    let num_cameras: u64 = u64::from_le_bytes(buffer[..idx+8].try_into().unwrap());
    idx += 8;
    println!("Found {} cameras", num_cameras);
    let mut cameras: Vec<Camera> = Vec::new();
    for _idx in 0..num_cameras{
        let camera_id = u32::from_le_bytes(buffer[idx..idx+4].try_into().unwrap());
        idx += 4;
        let model_id: CameraModelId = i32::from_le_bytes(buffer[idx..idx+4].try_into().unwrap()).into();
        idx += 4;
        let width = u64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let height = u64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let num_params: u64 = get_num_params(&model_id);
        let mut params: Vec<f64> = Vec::new();
        for _idx in 0..num_params {
            params.push(f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap()));
            idx += 8;
        }
        let camera: Camera = Camera{camera_id, model_id, width, height, params};
        cameras.push(camera)
    }
    return Ok(cameras);
}

#[allow(non_snake_case)]
pub fn read_points3D_bin(path: &str) -> io::Result<Vec<Point3D>> {

    // Open the file in read-only mode
    let mut file: File = File::open(path)?;

    // Read the contents of the file into a buffer
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer)?;
    // Do something with the contents of the buffer
    println!("Read {} bytes from the file", buffer.len());
    let mut idx: usize = 0;
    let num_points3D: u64 = u64::from_le_bytes(buffer[..idx+8].try_into().unwrap());
    idx += 8;
    println!("Found {} 3D points.", num_points3D);
    let mut points3D: Vec<Point3D> = Vec::new();
    for _pt in 0..num_points3D{
        let point3D_id = point3D_t::from_le_bytes(buffer[idx..idx+size_of::<point3D_t>()].try_into().unwrap());
        idx += size_of::<point3D_t>();
        let x = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let y = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let z = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let xyz = DVec3::new(x,y,z);

        let r = u8::from_le_bytes(buffer[idx..idx+1].try_into().unwrap());
        idx += 1;
        let g = u8::from_le_bytes(buffer[idx..idx+1].try_into().unwrap());
        idx += 1;
        let b = u8::from_le_bytes(buffer[idx..idx+1].try_into().unwrap());
        idx += 1;
        let color =  Color{r,g,b};

        let error = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;

        let track_length: u64 = u64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let mut track: Vec<TrackElement> = Vec::new();
        for _ in 0..track_length {
            
            let image_id: image_t = image_t::from_le_bytes(buffer[idx..idx+size_of::<image_t>()].try_into().unwrap());
            idx += size_of::<image_t>();
            #[allow(non_snake_case)]
            let point2D_idx: point2D_t = point2D_t::from_le_bytes(buffer[idx..idx+size_of::<point2D_t>()].try_into().unwrap()); 
            idx += size_of::<point2D_t>();
            track.push((image_id, point2D_idx));//TrackElement{image_id: image_id, point2D_idx: point2D_idx});
            
        }
        points3D.push(Point3D{point3D_id, xyz, color, error, track});
    }
    return Ok(points3D);
}

pub fn read_images_bin(path: &str) -> io::Result<Vec<Image>>{
    // Open the file in read-only mode
    let mut file: File = File::open(path)?;

    // Read the contents of the file into a buffer
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer)?;
    // Do something with the contents of the buffer
    println!("Read {} bytes from the file", buffer.len());
    let mut idx: usize = 0;
    let num_reg_images: u64 = u64::from_le_bytes(buffer[..idx+8].try_into().unwrap());
    idx += 8;
    println!("Found {} registered images.", num_reg_images);
    let mut images: Vec<Image> = Vec::new();
    for _im in 0..num_reg_images{
        let image_id = image_t::from_le_bytes(buffer[idx..idx+size_of::<image_t>()].try_into().unwrap());
        idx += size_of::<image_t>();

        
        let w = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let x = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let y = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let z = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let mut rot: DQuat = DQuat{x:x,y:y,z:z,w:w};
        rot = rot.normalize();
        let x = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let y = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let z = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let trans = DVec3::new(x,y,z);
        let camera_id = camera_t::from_le_bytes(buffer[idx..idx+size_of::<camera_t>()].try_into().unwrap());
        idx += size_of::<camera_t>();

        let mut name = String::new();
        while buffer[idx] != b'\0' {
            name.push(buffer[idx].try_into().unwrap());
            idx += 1;
        }
        idx += 1;
        
        let num_points2D = u64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
        idx += 8;
        let mut points2D: Vec<DVec2> = Vec::new();
        let mut point3D_ids: Vec<point3D_t> = Vec::new();
        for _idx in 0..num_points2D {
            let x = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
            idx += 8;
            let y = f64::from_le_bytes(buffer[idx..idx+8].try_into().unwrap());
            idx += 8;
            point3D_ids.push(point3D_t::from_le_bytes(buffer[idx..idx+8].try_into().unwrap()));
            idx += 8;
            points2D.push(DVec2{x,y});
        }
        let image = Image{image_id, camera_id, name, rot, trans, points2D, point3D_ids};
        images.push(image);
    }
    return Ok(images);
}