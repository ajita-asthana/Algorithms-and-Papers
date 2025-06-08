int firstDuplicate(int[] a) {
  int min_second_index = a.length 
  for(int i=0; i<a.length; i++) {
    for(int j=i+1; j<a.length; j++) {
      if (a[i] == a[j]) {
        min_second_index = Math.min(min_second_index, j);
      }
    }
  }
  if (min_second_index == a.length) 
      return -1;  
  else 
      tryutn a[min_second_index];
}
