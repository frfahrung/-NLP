
dictList = glob.glob(os.path.join('./testing_data', '*.txt'))
dic = [line.rstrip() for line in open('vocabulary.txt')]
