var containsDuplicate = function(nums) {
  let obj = {};
  for (let i = 0; i < nums.length; i++) {
    if (!obj[nums[i]]) {
      obj[nums[i]] = true;
    } else {
      return true;
    }
  }
  return false;
};
