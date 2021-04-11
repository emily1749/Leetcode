def meeting_planner(slotsA, slotsB, dur):

  '''
  
    0  10  15     50   60  70   120  140   210
    -------------------------------------------
  
  A     ------------    ----------    --------
  B ---------           ----
  
  idxA = 0
  idxB = 0
  how to compare the two
  how to know which one to increment
  
  time: O(max(A+B)) A - length slotsA B- len- slotsB
  space: O(1)
  
  [10, 50]
  [20, 150]
  
  idxB[1] compare to the starting of A
  
  1)
  A  ------
  B--------------
  2)
  A     ----------
  B---------
  3)
  A-----------
  B    ----
  4)
  A---------
  B     ---------
  5)
  A ----
  B          -----
  6)
  A          ----
  B-----
  
  first looking at the two start times, and the max of those two
  
  minimum of the two end times
  minimum of the two end times < max two start times, then theres no overlap
  else:
    check the duration, difference of the max and min, >= duration
  
  
  '''
  
  idxA = 0
  idxB = 0
  # slots A [60, 120]
  #Slots B [60, 70]
  while idxA < len(slotsA) and idxB < len(slotsB):
    print(idxA)
    print(idxB)
    #compare the start times to see which one starts first
    max_start = max(slotsA[idxA][0], slotsB[idxB][0]) #60
    min_end = min(slotsA[idxA][1], slotsB[idxB][1]) #70

    if min_end > max_start:
      curr_duration = min_end - max_start # 10
      if curr_duration >= dur:
        return [max_start, max_start + dur]
      #else:
        #increment one tat ends first
    #if min(slotsA[idxA][1], slots[idxB][1]):
    if min_end == slotsA[idxA][1]: #50
      idxA = idxA + 1
    else:
      idxB = idxB + 1 
      
  return []