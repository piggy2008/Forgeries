import os

if __name__ == '__main__':
    path = '/mnt/hdd/data/ty2/dresden_spliced'
    imgs = os.listdir(path)
    imgs_list = []
    gt_list = []
    for img in imgs:
        if 'rgb' in img:
            imgs_list.append(img)
        else:
            gt_list.append(img)

    print(list(imgs_list))
    print(list(gt_list))