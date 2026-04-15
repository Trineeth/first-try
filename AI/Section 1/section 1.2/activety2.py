import os

file_path = os.path.join(os.path.dirname(__file__), 'tetx.txt')

with open(file_path, 'r') as file_read:
    print("File in read mode - ")
    print(file_read.read())

with open(file_path, 'w') as file_write:
    file_write.write("THIS IS NOT LATIN, THIS IS RANDOM TEXT FROM THIS WEBSITE, https://loremipsum.io/generator/?n=9&t=p, Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.")
    file_write.write("FILE IN WRITE MODE --")

with open(file_path, 'a') as file_append:
    file_append.write("THIS IS NOT LATIN, THIS IS RANDOM TEXT FROM THIS WEBSITE, https://loremipsum.io/generator/?n=9999999999999999999999999999999999999999999999&t=p, Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.")
    file_append.write("FILE IN append MODE --")
