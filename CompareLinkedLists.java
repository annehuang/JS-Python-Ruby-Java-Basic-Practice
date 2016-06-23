int CompareLists(Node headA, Node headB) {
 
  Node ptr1;
  Node ptr2;
    
  for (ptr1 = headA, ptr2= headB; ptr1 != null && ptr2 != null; ptr1 = ptr1.next, ptr2 = ptr2.next){
      if (ptr1.data != ptr2.data)
          return 0;
      if ((ptr1.next == null && ptr2.next != null) || (ptr1.next != null && ptr2.next == null))
          return 0;
    }
    return 1;
}
