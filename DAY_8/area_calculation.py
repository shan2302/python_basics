def paint_calc(height,width,cover):
    total_number_of_cans =round((height*width)/cover)
    return total_number_of_cans
test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall:"))
coverage = 5

print(paint_calc(height=test_h,width=test_w,cover=coverage))


