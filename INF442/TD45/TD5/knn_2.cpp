#include "knn.h"
#include "mpi.h"
#include <iostream>
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

void Knn::NearestNeighbours(Mail* mail_to_classify, int* labels, int* distances) const 
{
  for(int i=0; i<k_; i++)
  {
     labels[i]=-1;
     distances[i]=std::numeric_limits<int>::max();        
  }
  
  for(int j=0;j<train_instances_->num_instances();j++)
  {
     Insert(labels,distances, mail_to_classify,train_instances_->instance(j));
  }
  


}

int Knn::ClassifyMpi(Mail* mail_to_classify) const 
{
   int rank,size;
   MPI_Status status;
   MPI_Comm_rank(MPI_COMM_WORLD, &rank);
   MPI_Comm_size(MPI_COMM_WORLD, &size);
   int n = train_instances_->num_instances()/size;
   
   int* labels = new int[k_];
   int* distances = new int[k_];
   	int* l= new int[k_];
   	int* d= new int[k_];
   InitNearestNeighbours(labels,distances);
   int partner;

   if(rank != (size -1)){      
   for(int i=rank*n; i<(rank*n+n); i++)
   {
      Insert(labels, distances, mail_to_classify, train_instances_->instance(i));
   }
	}
   
   if(rank == (size -1)){      
   for(int i=rank*n; i<train_instances_->num_instances(); i++)
   {
      Insert(labels, distances, mail_to_classify, train_instances_->instance(i));
   }
	}
   for(int m = size; m>1; m=m-m/2)
   {
      if(m%2==0)
      {
         if((m/2<=rank)&&(rank<m))
         {
            partner = rank-m/2;
            MPI_Send(labels, k_, MPI_INT, partner, rank, MPI_COMM_WORLD);
            MPI_Send(distances, k_, MPI_INT, partner, rank+size, MPI_COMM_WORLD);


		std::cout << "send from" << rank << "to" << partner << endl;
         }
         else if((rank<m/2)) 
         {
            partner = rank+m/2;
            MPI_Recv(l, k_, MPI_INT, partner, rank, MPI_COMM_WORLD, &status); 
            MPI_Recv(d, k_, MPI_INT, partner, rank+size, MPI_COMM_WORLD, &status); 
		std::cout << "receive of" << rank << "from" << partner << endl;
            Merge(labels,distances,l,d);
	   

         }
      }
      else
      {
         if((m/2<rank)&&(rank<m))
         {
            partner = rank-m/2;
            MPI_Send(labels, k_, MPI_INT, partner, rank, MPI_COMM_WORLD);
            MPI_Send(distances, k_, MPI_INT, partner, rank+size, MPI_COMM_WORLD);
		std::cout << "send from" << rank << "to" << partner << endl;
         }
        else if((rank > 0)&&(rank<=m/2))
         {
            partner = rank+m/2;
            MPI_Recv(l, k_, MPI_INT, partner, rank, MPI_COMM_WORLD, &status); 
            MPI_Recv(d, k_, MPI_INT, partner, rank+size, MPI_COMM_WORLD,&status); 
		std::cout << "receive of" << rank << "from" << partner << endl;
            Merge(labels,distances,l,d);
         }
         
      }

   }
      return PredictedLabel(labels);
   
   
}
int Knn::PredictedLabel(int* labels, double threshold) const {
  double sum = 0.0;
  for(int i=0; i<k_; i++)
  {
     sum += (double)labels[i]/(double)k_;
  }
  
  if(sum>=threshold)
     return 1;
  else
     return 0;
}

void Knn::Insert(int* labels, int* distances, Mail* mail_to_classify,
        Mail* train_mail) const       
{
   int d = mail_to_classify->Distance(train_mail);
   int l = train_mail->label();
   for(int i=0; i<k_; i++)
   {
      if(d<distances[i])
      {
         for(int j=i; j<k_; j++)
         {
            int d_tem = distances[j];
            int l_tem = labels[j];
            distances[j] = d;
            labels[j]= l;
            d = d_tem;
            l = l_tem;
         }
         break;
      }
      
   }

}

