# -*- coding: utf-8 -*-
MAX_ITERATIONS = 100

def k_means(data,centroids,old_centroids,clusters,k):
    iterations = 0

    while not has_converged(centroids,old_centroids,iterations):
        iterations = iterations +1
        clusters = [[] for i in range(k)]
        clusters = cluster_assignments(data,centroids,clusters)
        centroids = calculate_centroids(data,centroids,clusters)

        print "iteration %d " %iterations
        for i in range (0,len(clusters)):
            print i,clusters[i]
    return clusters
def cluster_assignments(data,centroids,clusters):

    for value in data:
        point_assignments = min(centroids, key=lambda x:abs(x-value))
        index = centroids.index(point_assignments)

        if value not in clusters[index]:
            try:
                clusters[index].append(value)
            except KeyError:
                clusters[index] = [value]
    return clusters

def calculate_centroids(data,centroids,clusters):
    index = 0

    for key in clusters:
        old_centroids[index] = centroids[index]
        centroids[index] = reduce(lambda x, y: x + y, key) / len(key)
        index +=1

    return centroids

def has_converged(centroids, old_centroids,iterations):
    if iterations > MAX_ITERATIONS:
        return True
    return old_centroids == centroids

def format_output(clusters):
    output = ""
    for value in data:
        for i in range (0,len(clusters)):
            if value in clusters[i]:
                output =  output+'\n' +"Point "+str(value) + " is in cluster "+ str(i)
    return output

#data = [1.8, 4.5, 1.1, 2.1, 9.8, 7.6, 11.32, 3.2, 0.5, 6.5]

input_file = "prog2-input-data.txt"
output_file = "prog2-output-data.txt"

#input_file = raw_input("Enter the name of the input file: ")
#output_file = raw_input("Enter the name of the output file: ")
f = open(input_file)
data = []
for line in f:
    data.append(float(line.rstrip()))
k = int(raw_input("Enter the number of clusters k : "))

clusters = [[] for i in range(k)]
centroids = data[0:k]
old_centroids = [[] for i in range(k)]
clusters = k_means(data,centroids,old_centroids,clusters,k)
fo = open(output_file ,'w+')
output_string = format_output(clusters)
fo.write(output_string)
fo.close()
