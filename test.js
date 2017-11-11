const SmileFaceDetector = require('smile-face-detector');
const detector = new SmileFaceDetector({smileScale: 1.01, smileNeighbor: 50});
detector.on('error', (error) => {
  console.error(error);
});
detector.on('face', (faces, image) => {
  console.log(faces);
  faces.forEach((face) => {
    // write rectangle
    image.rectangle([face.x, face.y], [face.width, face.height], SmileFaceDetector.green, 2);
  });
});
detector.on('smile', (smiles, face, image) => {
  console.log(smiles);
  smiles.forEach((smile) => {
    image.rectangle([smile.x + face.x, smile.y + face.height/2 + face.y], [smile.width, smile.height], SmileFaceDetector.blue, 2);
  });
  image.save('./images/Lenna_result.jpg');
});
detector.load('/Users/Nathan/OneDrive/Code/codestellation/images/angry.jpg').then((image) => {
  detector.detect(image);
}).catch((e) => {
  console.error(e);
});