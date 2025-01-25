class Solution {
public:
    int isSafe(vector<vector<int>>& graph, vector<int>& safe, int ind, vector<int>& terminal) {
        if (terminal[ind] == 1) {
            return true;
        }
        if (safe[ind] != -1) { //this line is used to check if the node is already visisted or not
            return safe[ind] == 1;
        }
        safe[ind] = 0;  //this line is very important to mark the nodes as visited and to avoid the proble of cyclic graphs
        for (int k = 0; k < graph[ind].size(); k++) {
            int result = isSafe(graph, safe, graph[ind][k], terminal);  // Use graph[ind][k]
            if (!result) {
                // safe[ind] = 0;
                return false;
            }
        }
        safe[ind] = 1;
        return true;
    }

    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        vector<int> safe(graph.size(), -1);
        vector<int> terminal(graph.size(), 1);
        for (int i = 0; i < graph.size(); i++) {
            if (graph[i].size() > 0) {
                terminal[i] = 0;
            }
        }
        vector<int> result;
        for (int i = 0; i < graph.size(); i++) {
            if (isSafe(graph, safe, i, terminal)) {  // Check if the node is safe
                result.push_back(i);
            }
        }
        return result;
    }
};
