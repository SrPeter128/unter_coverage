import sys

def readin(start, ende, scaff):
	infile = sys.argv[1]
	with open (infile) as raw:
		cut_list = []
		for line in raw:
			temp_row = line.rstrip().split()
			if len(temp_row) > 0:
				if temp_row[0] == scaff and int(temp_row[1]) >= int(start) and int(temp_row[1]) <= int(ende):
					cut_list.append(temp_row)
				#elif int(temp_row[1]) > int(ende): hier könnte man das ganze vielleicht noch ein bisschen schneller machen... 
				#	break
	return cut_list

def under_coverage(cut_list):
	list_len = len(cut_list)
	all_reads = 0
	for i in range(0,len(cut_list)):
		all_reads += int(cut_list[i][2])
	#print("Berreichslaenge:", list_len,  "Total_Reads: ",  all_reads)
	#print(cut_list)
	if list_len > 0:
		return float(all_reads)/float(list_len)
	else:
		scaff = sys.argv[2]
		start = sys.argv[3]
		stop = sys.argv[4]
		print("Im angegebenen Bereich " + scaff + " konnten die Positionen " + start + " bis " + stop + " nicht gefunden werden.")
		exit()


def main():

	scaff = sys.argv[2]
	start = sys.argv[3]
	stop = sys.argv[4]
	cut_list = readin(start, stop, scaff)
	under_cover = under_coverage(cut_list)
	outstr = "Im Bereich " + scaff +  " zwischen " + str(start) + " und " + str(stop) + " wurden durchschnittlich " + str(under_cover) + " Reads gefunden."
	print(outstr)
if __name__ == '__main__':
	main()
