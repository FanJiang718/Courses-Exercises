#include "knn.h"
#include "mpi.h"

#include <cstdio>
#include <limits>

using namespace std;

int Knn::Classify(Mail* mail_to_classify) const {
    int* labels = new int[k_];
    int* distances = new int[k_];
    this->InitNearestNeighbours(labels, distances);

    this->NearestNeighbours(mail_to_classify, labels, distances);

    int label = PredictedLabel(labels);

    // Frees the allocated memory
    delete[] labels;
    delete[] distances;

    return label;
}

void Knn::Classify(Mail* mail_to_classify, double* thresholds, int* predicted_labels, int num_predictions) const {
    int* labels = new int[k_];
    int* distances = new int[k_];
    this->InitNearestNeighbours(labels, distances);

    this->NearestNeighbours(mail_to_classify, labels, distances);

    for (int i = 0; i < num_predictions; i++) {
        predicted_labels[i] = PredictedLabel(labels, thresholds[i]);
    }

    // Frees the allocated memory
    delete[] labels;
    delete[] distances;
}

void Knn::InitNearestNeighbours(int* labels, int* distances) const {
    // Arrays to store the k nearest neighbours
    for (int i = 0; i < k_; ++i) {
        labels[i] = -1;
        distances[i] = std::numeric_limits<int>::max();
    }
}




void Knn::Merge(int* local_labels, int* local_distances,
        const int* other_labels, const int* other_distances) const{
  int cur_local = k_;
    int cur_other = k_;
    // Gets rid of the neighbours which are too far away
    while (cur_local + cur_other > k_) {
        if (local_distances[cur_local-1] > other_distances[cur_other-1]) {
            cur_local--;
        } else {
            cur_other--;
        }
    }
    // Merges the two arrays in the local one
    while (cur_local || cur_other ) {
        if (!cur_local || (cur_other &&
                    local_distances[cur_local-1] <= other_distances[cur_other-1])) {
            cur_other--;
            local_distances[cur_local + cur_other] = other_distances[cur_other];
            local_labels[cur_local + cur_other] = other_labels[cur_other];
        } else {
            cur_local--;
            local_distances[cur_local + cur_other] = local_distances[cur_local];
            local_labels[cur_local + cur_other] = local_labels[cur_local];
        }
    }
}


int Knn::PredictedLabel(int* labels) const {
    int num_spam = 0;
    int num_ham = 0;
    for (int i = 0; i < k_; ++i) {
        switch(labels[i]) {
            case 0:
                num_ham++;
                break;
            case 1:
                num_spam++;
                break;
            default:
                break;
        }
    }
    return num_spam > num_ham ? 1 : 0;
}

void Knn::NearestNeighbours(Mail* mail_to_classify, int* labels, int* distances) const {
  // TODO
  for(int i =0 ; i < train_instances_->num_instances();i++){
	Insert(labels,distances,mail_to_classify,train_instances_->instance(i));
}
}

int Knn::ClassifyMpi(Mail* mail_to_classify) const {
  // TODO
  	int rank;
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
  	int size;
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	int k = train_instances_->num_instances()/size;
	
    int* labels = new int[k_];
    int* distances = new int[k_];
    this->InitNearestNeighbours(labels, distances);
	int i;
	if(rank!= (size-1)){
	for(i = rank*k; i < (rank+1)*k; i++){
    		this->Insert(labels, distances,mail_to_classify,train_instances_->instance(i));
	}
	}
	if(rank == (size-1)){
	        for(i = rank*k; i < train_instances_->num_instances(); i++){
                	this->Insert(labels, distances,mail_to_classify,train_instances_->instance(i));
        	}
	
	}
	if(rank!= 0){

		MPI_Send(labels,k_,MPI_INT,0,rank, MPI_COMM_WORLD);
		MPI_Send(distances,k_,MPI_INT,0,rank+size, MPI_COMM_WORLD);
	}
 int predicted;
  if(rank == 0){
		for(int j = 1; j< size; j++){
			int* other_labels = new int[k_];
			int* other_distances = new int[k_];
			MPI_Recv(other_labels,k_,MPI_INT,j,j,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
			MPI_Recv(other_distances,k_,MPI_INT,j,j+size,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
			Merge(labels,distances,other_labels,other_distances);
			delete [] other_labels;	
			delete [] other_distances;
		}
		
	}
	
	predicted = PredictedLabel(labels);
	delete [] labels;
	delete [] distances;
  return predicted;
}
int Knn::PredictedLabel(int* labels, double threshold) const {
  // TODO
  double count = 0;
  for(int i =0; i< k_; i++){
	count += labels[i];
}
  if(count >=(k_ * threshold)) return 1;
  return 0;
}

void Knn::Insert(int* labels, int* distances, Mail* mail_to_classify,
        Mail* train_mail) const {
	  // TODO
	int dist = train_mail->Distance(mail_to_classify);
	for(int i=0; i<k_; i++){
		if(dist<distances[i]){
			for(int j =k_-1; j>i ; j--){
				distances[j] = distances[j-1];
				labels[j] = labels[j-1];
			}
			distances[i] = dist;
			labels[i] = train_mail->label();
			break;
		}
	}
}

