from data_processor import reader,writer

data = reader.read_data('test.txt')
print('test.txt : ',data)
writer.write_data("Hello Good ",'test.txt')