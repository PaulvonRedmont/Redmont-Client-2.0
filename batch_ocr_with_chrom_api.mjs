import Lens from 'chrome-lens-ocr';
import { inspect } from 'util';

const lens = new Lens();
const log = data => console.log(inspect(data, { depth: null, colors: true }));

// Replace 'shrimple.png' with the path to your image file
lens.scanByFile("C:\\Users\\paul\\Downloads\\40ab2c60-1d03-11ef-be0f-e3c26f9cdbe9.png").then(log).catch(console.error);
