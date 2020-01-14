import java.util.*;
public class StableMatching implements StableMatchingInterface{
	
	//////////////////////////////////////////////////////////////////////////////////////
	// We use Pair to represent the partners of a certain group of women.
	// Pair.group represent the group of the man that a certain group of women engaged.
	// Pair.position represent the position of this group of men in her preference list.
	public class Pair implements Comparable<Pair>{
		int group;
		int position;
		
		public Pair(int group, int position){
			this.group = group;
			this.position = position; 
		}
		// To insert Pairs into priority queue, we define the compareTo,
		// so that the least attractive man is on the peek of priority queue.
		public int compareTo(Pair o){
			if(this.position > o.position) return -1;
			else if(this.position == o.position) return 0;
			else return 1;
		}

	}
	
	//We use Group_man to represent a certain group of men. 
	//Group represents the number of this group.
	// unengaged represents the number of unengaged men in this group.
	// positionInWomenPreference represents this group's position in each woman group's preference list.
	// so positionInWomenPreference is int[w].
	public class Group_man implements Comparable<Group_man>{
		int group;
		int unengaged;
		int[] positionInWomenPreference;
		
		public Group_man(int group, int unengaged, int[] positionInWomenPreference){
			this.group = group;
			this.unengaged = unengaged;
			this.positionInWomenPreference = positionInWomenPreference;
		}
		
		public int compareTo(Group_man o){
			if(this.unengaged > o.unengaged) return -1;
			else if(this.unengaged == o.unengaged) return 0;
			else return 1;
		}

	}
	/////////////////////////////////////////////////////////////////
	
	public int[][] constructStableMatching (int[] menGroupCount, 
			int[] womenGroupCount, 
			int[][] menPrefs, 
			int[][] womenPrefs){
		
		int m = menGroupCount.length;
		int w = womenGroupCount.length;
		int unengaged_men = 0;
		int[] man_notasked = new int[m]; // the woman group that man is going to propose
		int[][] result = new int[m][w];
		PriorityQueue<Group_man> queue = new PriorityQueue<Group_man>();
		// we use queue to select the man group who has the most unengaged men
		
		// We creat the MenPositionInWomenPrefs to record the position of each man group
		// in each woman group's preference list. This step allows us to compare man group i 
		// and man group i' in a certain woman's preference list with complexity O(1).
		int[][] MenPositionInWomenPrefs = new int[m][w];
		for(int j =0; j< w; j++){
			for(int i=0; i< m; i++){
				MenPositionInWomenPrefs[womenPrefs[j][i]][j] = i;
			}
		}
		// initialization
		for(int i=0; i< m; i++){
			man_notasked[i] = 0;
			unengaged_men += menGroupCount[i];
			Group_man tmp_groupman = new Group_man(i,menGroupCount[i],MenPositionInWomenPrefs[i]);
			for(int j=0; j<w;j++){
				result[i][j] = 0;
			}
			queue.add(tmp_groupman);
		}
		// we use this Hash map to record the group number and its position in preference list
		// for engaged partners of each woman group
		HashMap<Integer, PriorityQueue<Pair>> woman_EngagedMenGroups = new HashMap<Integer, PriorityQueue<Pair>>();
		for(int j =0; j< w; j++){
			PriorityQueue<Pair> engagedMenGroups = new PriorityQueue<Pair>();
			woman_EngagedMenGroups.put(j, engagedMenGroups);
		}
		
		// Algorithm
		while(unengaged_men>0){
			Group_man man = queue.poll();
			int group_man = man.group;
			if(menGroupCount[group_man] <=0) continue;
			int group_woman = menPrefs[group_man][man_notasked[group_man]];
			if(womenGroupCount[group_woman] >0){
				int n = Math.min(menGroupCount[group_man], womenGroupCount[group_woman]);
				if(result[group_man][group_woman]==0){
					int manPositionInWomanPreferenceList= man.positionInWomenPreference[group_woman];
					woman_EngagedMenGroups.get(group_woman).add(new Pair(group_man,manPositionInWomanPreferenceList));
				}
				
				result[group_man][group_woman] += n;
				unengaged_men -=n;
				menGroupCount[group_man] -=n;
				womenGroupCount[group_woman] -=n;
				if(menGroupCount[group_man]!=0){
					man.unengaged = menGroupCount[group_man];
					queue.add(man);
				}
				
			}
			else{
				Pair tmp_pair = woman_EngagedMenGroups.get(group_woman).poll();
				int manPositionInWomanPreferenceList_ii = tmp_pair.position;
				int ii = tmp_pair.group;
				int manPositionInWomanPreferenceList_i = man.positionInWomenPreference[group_woman];
				if(manPositionInWomanPreferenceList_i < manPositionInWomanPreferenceList_ii){
					int n = Math.min(menGroupCount[group_man], result[ii][group_woman]);
					
					if(result[group_man][group_woman]==0){
						// if result[group_man][group_woman]==0, this means they did not engage before,
						// so now we need to add group_man in group_woman's partners list.
						Pair tmp_pair_i = new Pair(group_man,manPositionInWomanPreferenceList_i);
						woman_EngagedMenGroups.get(group_woman).add(tmp_pair_i);
					}
					result[group_man][group_woman] +=n;
					result[ii][group_woman] -=n;
					menGroupCount[group_man] -=n;
					menGroupCount[ii] +=n;
					
					if(menGroupCount[group_man]!=0){
						man.unengaged = menGroupCount[group_man];
						queue.add(man);
					}
					if(menGroupCount[ii]!=0){
						queue.add(new Group_man(ii,menGroupCount[ii],MenPositionInWomenPrefs[ii] ));
					}
					
					if(result[ii][group_woman] >0){
						//if result[ii][group_woman] >0, we need add ii into group_woman's partners list,
						// because we have polled it at the beginning of iteration.
						woman_EngagedMenGroups.get(group_woman).add(tmp_pair);
					}
					
				}
				else{
					// if group_man is rejected by group_woman, he will not ask group_woman anymore,
					// so we plus man_notasked[group_man] by 1, to represent move one step in
					// his preference list.
					queue.add(man);
					woman_EngagedMenGroups.get(group_woman).add(tmp_pair);
					man_notasked[group_man] +=1;
				}
				
			}
		}
		return result;
	}
	
}
