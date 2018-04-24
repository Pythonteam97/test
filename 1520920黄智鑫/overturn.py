def overturn(a):
	if len(a)<1:
		return a
	return overturn(a[1:])+a[0]
