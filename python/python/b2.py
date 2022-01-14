n = int(input("Nhập n: "));
tong = 0;
while(n>0):
	tong = tong + n%10;
	n = int(n / 10);
print(tong)
ten = input("Nhập tên của bạn: ");
print(ten);
print(len(ten.replace(' ','')));