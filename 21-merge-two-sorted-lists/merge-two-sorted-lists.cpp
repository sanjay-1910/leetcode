/**
 * Definition for singly-linked temp.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* temp = list1;
        ListNode* temp2 = list2;
        ListNode* fina = new ListNode(0);
        ListNode* current = fina;
        while (temp != NULL && temp2 != NULL) {
            if (temp->val <= temp2->val) {
                current->next = new ListNode(temp->val);
                temp = temp->next;
            } else {
                current->next = new ListNode(temp2->val);
                temp2 = temp2->next;
            }
            current = current->next;
        }
        if (temp != NULL) {
            current->next = temp;
        } else {
            current->next = temp2;
        }
        ListNode* mergedList = fina->next;
        delete fina;
        return mergedList;
    }
};
