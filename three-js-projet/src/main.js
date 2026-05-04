import * as THREE from 'three';




// Initialisation du moteur de rendu
function main(){
    const canvas = document.querySelector('#c')
    const renderer = new THREE.WebGLRenderer({'antialias': true, canvas});



// La Caméra
const fov = 75;
const aspect = 2;
const near = 0.1;
const far = 5;
const camera = new THREE.PerspectiveCamera(fov, aspect, near, far)
camera.position.z = 2;
// camera.position.y = -0.1;

// La Scène et le Cube

const scene = new THREE.Scene();

const geometry = new THREE.BoxGeometry(1, 0.2, 1);
const material = new THREE.MeshPhongMaterial({color: 0x44aa88})

const cube = new THREE.Mesh(geometry, material);
const cube1 = new THREE.Mesh(geometry, material);

scene.add(cube)
scene.add(cube1)


// Animation et Lumière 

const light = new THREE.DirectionalLight(0xff0000, 100)
light.position.set(-1, 2, 4)
scene.add(light)


function render(time){
    time *=0.001;

    cube.rotation.x = time
    cube.rotation.y = time;

    renderer.render(scene, camera)
    requestAnimationFrame(render);
}
requestAnimationFrame(render);

}

main()