/**
 * Definition for singly-linked list.
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int c=0;
        int i=0;
        ListNode* temp=head;
        while(temp!=NULL)
        {
            c=c+1;
            temp=temp->next;
        }
         if(c==n)
         {
             return head->next;
         }
         ListNode* temp2=head;
         while(i<(c-(n+1)) && temp2->next!=NULL)
         {
            temp2=temp2->next;
            i=i+1;
    }
       if(temp2->next==NULL)
       {
           return head;
       }
     if(temp2->next->next==NULL)
      {
          temp2->next=NULL;
          return head;
      }
     else
     {
         temp2->next=temp2->next->next;
         return head;
     }
    }

};