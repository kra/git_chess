# get files from http://cap.connx.com/a-openings/ etc

def split_file(file_name):
    """ split PGN opening file into single PGN games """
    file_no = 0
    (prefix, suffix) = file_name.split('.')
    out_file = open(file_name)          # just to have a file handle
    for line in open(file_name).readlines():
        if line.find('[Event') == 0:
            out_file.close()
            out_file = open('%s_%s.%s' % (prefix, file_no, suffix), 'w')
            file_no += 1
        out_file.write(line)
        

if __name__ == '__main__':
    split_file('A00.pgn')
