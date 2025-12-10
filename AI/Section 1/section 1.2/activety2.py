file_read = open('C:/Users/trine/OneDrive/Documents/python class/AI/Section 2/tetx.txt', 'r')

print("File in read mode - ")
print(file_read.read())
file_read.close()

file_write = open('C:/Users/trine/OneDrive/Documents/python class/AI/Section 2/tetx.txt', 'w')

file_write.write("THIS IS NOT LATIN, THIS IS RANDOM TEXT FROM THIS WEBSITE, https://loremipsum.io/generator/?n=9&t=p, Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.")
file_write.write("FILE IN WRITE MODE --")

file_append = open('C:/Users/trine/OneDrive/Documents/python class/AI/Section 2/tetx.txt', 'a')

file_append.write("THIS IS NOT LATIN, THIS IS RANDOM TEXT FROM THIS WEBSITE, https://loremipsum.io/generator/?n=9999999999999999999999999999999999999999999999&t=p, Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.")
file_append.write("FILE IN append MODE --")



file_append.close()
