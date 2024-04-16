import numpy as np

from PIL import Image
from tqdm import tqdm

from torch.utils.data import DataLoader

from openst.preprocessing.CUT.models import create_model
from openst.preprocessing.CUT.options.test_options import TestOptions

def create_dataset(opt):
    data_loader = OpenSTDatasetDataLoader(opt)
    dataset = data_loader.load_data()
    return dataset

class OpenSTDatasetDataLoader():
    """Wrapper class of Dataset class that performs multi-threaded data loading"""

    def __init__(self, image_tiles):
        self.image_tiles = image_tiles
        self.dataloader = DataLoader(
            self.image_tiles,
            batch_size=1,
            shuffle=False,
            num_workers=1,
            drop_last=False,
        )

    def load_data(self):
        return self

    def __len__(self):
        """Return the number of data in the dataset"""
        return len(self.image_tiles)

    def __iter__(self):
        """Return a batch of data"""
        for i, data in enumerate(self.dataloader):
            yield data

def _images_to_tiles(img):
    _img_shape = img.shape
    tiles = []
    for x in range(0, _img_shape[0]-args.tile_size_px, args.tile_size_px):
        for y in range(0, _img_shape[1]-args.tile_size_px, args.tile_size_px):
            tiles.append([x, y])

    imgs = []
    for i, coord in tqdm(enumerate(tiles)):
        imgs.append(img[coord[0]:(coord[0]+args.tile_size_px), coord[1]:(coord[1]+args.tile_size_px)])

    return tiles, imgs 


def _tiles_to_images(tiles, imgs, dest_shape):
    img_restitch = np.zeros(dest_shape)
    for i, coord in tqdm(enumerate(tiles)):
        img_restitch[coord[0]:(coord[0]+args.tile_size_px), coord[1]:(coord[1]+args.tile_size_px)] = imgs[i] 


def _image_preprocess(model, dataset):
    model.data_dependent_initialize(dataset[0])
    model.eval()
    
    output = []
    for data in dataset:
        data = {'A': None, 'B': None, 'A_paths': None, 'B_paths': None}
        model.set_input(data)
        model.test()
        output += [model.get_current_visuals()]
    
    return output


def _run_image_preprocess(args):
    Image.MAX_IMAGE_PIXELS = 933120000

    # Load image and get shape
    # TODO: load from h5 file, or load from lazy object
    img = np.array(Image.open(args.input_img))
    _img_shape = img.shape

    tiles, imgs_tiles = _images_to_tiles(img)

    opt = TestOptions().parse()
    opt.num_threads = 1
    opt.batch_size = 1
    opt.serial_batches = True
    opt.no_flip = True
    opt.load_size = args.tile_size_px

    model = create_model(opt)
    model.setup(opt)
    model.parallelize()

    dataset = create_dataset(imgs_tiles)
    imgs_tiles_processed = _image_preprocess(model, dataset)

    img_restitch = _tiles_to_images(tiles, imgs_tiles_processed, _img_shape)
    Image.fromarray(img_restitch.astype(np.uint8)).save(args.output_img)

if __name__ == "__main__":
    from openst.cli import get_image_preprocess_parser
    args = get_image_preprocess_parser().parse_args()
    _run_image_preprocess(args)