ten = input(" Nhap ten cua ban: ")
print(ten)
n = [];
dem = 0;
for i in ten:
  if i != ' ':
    dem+=1;
  else:
    n.append(str(dem))
    dem=0;
n.append(str(dem))
print(n);
str1 = n;     
str2 = str1[::-1];
if (str1 == str2):
  print("Có thuận nghịch");
else:
  print("Ko thuận nghịch");
print(str2)