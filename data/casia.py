import os

parser = argparse.ArgumentParser(description='SeeDataset')
parser.add_argument('--train-data-dir', type=str, default='/home/zhangxifan/simplex/dataset/CASIA_WebFace_182')
args = parser.parse_args()

class_list = os.listdir(args.train_data_dir)
for c in class_list:
    class_dir = os.path.join(args.train_data_dir, c)
    img_list = os.listdir(class_dir)
    for img in img_list:
        img_path = os.path.join(class_dir, img)
        print (img_path)
