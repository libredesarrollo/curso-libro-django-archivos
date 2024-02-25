from django.shortcuts import render

import csv

# def csv_read(request):
#     filename="documents\Libro1.csv"
   
#     try:
#         file = open(filename)
#         csv_reader = csv.reader(file, delimiter=";")
        
#         t = render(request, 'csv.html', {'csv_reader': csv_reader})
#         file.close()
#         return t
        
#     except (IOError) as error:
#         print("Error {}".format(error))
    
def csv_read(request):
    filename="documents\Libro1.csv"
   
    try:
        with open(filename) as file:
            csv_reader = csv.reader(file, delimiter=";")
            
            t = render(request, 'csv.html', {'csv_reader': csv_reader})
            return t
        
    except (IOError) as error:
        print("Error {}".format(error))
    
    

def csv_read_dict(request):
    filename="documents\Libro1.csv"
   
    try:
        file = open(filename)
        csv_reader = csv.DictReader(file, delimiter=";")

        for record in csv_reader:
            print(type(record))
            print(record)
            print(record.get('Nombre'))
        t = render(request, 'csv.html', {'csv_reader': csv_reader})
        file.close()
        return t

    except (IOError) as error:
        print("Error {}".format(error))

def csv_write(request):
    filename="documents\Libro2.csv"
   
    try:
        file = open(filename, 'w', newline='')
        csv_writer = csv.writer(file, delimiter=",")

        print(type(csv_writer))

        csv_writer.writerow([ 'Movie 1','Movie 2', 'Movie 3' ])
        csv_writer.writerow([ 'Avengers 1','Avengers 2', 'Avengers 3' ])
        file.close()
        return render(request, 'csv.html')

    except (IOError) as error:
        print("Error {}".format(error))

def csv_write_dict(request):
    filename="documents\Libro2.csv"
   
    try:
        file = open(filename, 'w', newline='')
        csv_writer = csv.DictWriter(file, delimiter=",", fieldnames=['name','surname'])

        print(type(csv_writer))

        csv_writer.writeheader()
        csv_writer.writerow( { 'name': 'andres', 'surname': 'cruz' } )
        file.close()
        return render(request, 'csv.html')

    except (IOError) as error:
        print("Error {}".format(error))
    
    
