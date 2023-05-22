from py3dbp import Packer, Bin, Item

packer = Packer()

packer.add_bin(Bin('small-envelope', 11.5, 6.125, 0.25, 10))
packer.add_bin(Bin('large-envelope', 15.0, 12.0, 0.75, 15))
packer.add_bin(Bin('small-box', 8.625, 5.375, 1.625, 70.0))
packer.add_bin(Bin('medium-box', 11.0, 8.5, 5.5, 70.0))
packer.add_bin(Bin('medium-2-box', 13.625, 11.875, 3.375, 70.0))
packer.add_bin(Bin('large-box', 12.0, 12.0, 5.5, 70.0))
packer.add_bin(Bin('large-2-box', 23.6875, 11.75, 3.0, 70.0))



packer.add_item(Item('[item 1]', 3.9370, 1.9685, 1.9685, 1))
packer.add_item(Item('[item 2]', 3.9370, 1.9685, 1.9685, 2))
packer.add_item(Item('[item 3]', 3.9370, 1.9685, 1.9685, 3))
packer.add_item(Item('[item 4]', 7.8740, 3.9370, 1.9685, 4))
packer.add_item(Item('[item 5]', 7.8740, 3.9370, 1.9685, 5))
packer.add_item(Item('[item 6]', 7.8740, 3.9370, 1.9685, 6))
packer.add_item(Item('[item 7]', 7.8740, 3.9370, 1.9685, 7))
packer.add_item(Item('[item 8]', 7.8740, 3.9370, 1.9685, 8))
packer.add_item(Item('[item 9]', 7.8740, 3.9370, 1.9685, 9))



packer.pack()
#displaying bins information:

# for b in packer.bins:
#     # print bin information
#     print(":::::::::::", b.string())

#     print("FITTED ITEMS:")
#     for item in b.items:
#         print("====> ", item.string())

#     print("UNFITTED ITEMS:")
#     for item in b.unfitted_items:
#         print("====> ", item.string())

#     print("***************************************************")
#     print("***************************************************")
    
# container
packer1 = Packer()
packer1.add_bin(Bin('container', 40, 100, 100, 700))

packer1.add_item(Item('bin 1',11.5, 6.125, 0.25, 10))
packer1.add_item(Item('bin-2', 15.0, 12.0, 0.75, 15)) 
packer1.add_item(Item('bin-3', 8.625, 5.375, 1.625, 70.0))
packer1.add_item(Item('bin-4', 11.0, 8.5, 5.5, 70.0))
packer1.add_item(Item('bin-5', 13.625, 11.875, 3.375, 70.0))
packer1.add_item(Item('bin-6', 12.0, 12.0, 5.5, 70.0))
packer1.add_item(Item('bin-7', 23.6875, 11.75, 3.0, 70.0))

packer1.pack()
# orientation of bins in container 
for b in packer1.bins:
    # print bin information
    print(":::::::::::", b.string())

    print("FITTED ITEMS:") 
    for item in b.items:
        print("====> ", item.string())

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())

    print("***************************************************")
    print("***************************************************")
