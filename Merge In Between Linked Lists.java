class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode temp1 = list1;
        for (int i = 1; i < a; i++)
            temp1 = temp1.next;
        
        ListNode temp2 = temp1;
        for (int i = a; i <= b; i++)
            temp2 = temp2.next;
        
		temp1.next = list2;
        while (list2.next != null)
            list2 = list2.next;
        
        list2.next = temp2.next;
        return list1;
    }
}