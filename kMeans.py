# -*- coding: utf-8 -*-
MAX_ITERATIONS = 5
def k_means_algorithm(data,centroids,clusters):
    old_centroids = dict(zip(range(k),range(k)))

    iterations = 0
    #check to see if the means have converged
    while not has_converged(centroids, old_centroids,iterations):

        iterations = iterations +1

        #create a list if lists to hold the points in different clusters
        clusters = dict(zip(range(k),[[] for i in range(k)]))

        #assign points to clusters
        clusters = cluster_assignments(data,centroids,clusters)

        #calculate means based on the new cluster
        centroids = recalculate_centroids(data,centroids,old_centroids,clusters)

        print "iteration %d " %iterations
        for i in range (0,len(clusters)):
            print i,clusters[i]

    return clusters

def has_converged(centroids, old_centroids,iterations):
    if iterations > MAX_ITERATIONS:
        return True
    return old_centroids == centroids


def recalculate_centroids(data,centroids,old_centroids,clusters):
    index = 0
    for key,value in clusters.iteritems():
        old_centroids[index] = centroids[index]
        centroids[index] = sum(value)/(len(value))
        index +=1
    return centroids

def cluster_assignments(data,centroids,clusters):
    for values in data:
        point_assignments = min(centroids.values(), key=lambda x:abs(x-values))

        for k,v in centroids.iteritems():
            if v == point_assignments:
                index = k
        clusters[index].append(values)
    return clusters

#Function that formats the output to the specified requirements
def format_output(clusters):
    output = ""
    for value in data:
        for i in range (0,len(clusters)):
            if value in clusters[i]:
                output =  output+'\n' +"Point "+str(value) + " is in cluster "+ str(i)
    return output

#Get the names of the input and output files from user
input_file = raw_input("Enter the name of the input file: ")

output_file = raw_input("Enter the name of the output file: ")

#read from file and add to the list data[]
f = open(input_file)
data = []
data = [float(x.rstrip()) for x in open(input_file)]
f.close()


k = int(raw_input("Enter the number of clusters: "))

#Initialize clusters and centroids

clusters = dict(zip(range(k),[[] for i in range(k)]))
centroids = dict(zip(range(k),data[0:k]))

#call kMeans algorithm

clusters = k_means_algorithm(data,centroids,clusters)

#format the output
fo = open(output_file ,'w+')
output_string = format_output(clusters)

#write the output to file
fo.write(output_string)

#print the output to console
print output_string

fo.close()
