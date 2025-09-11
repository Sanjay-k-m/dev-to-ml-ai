// var defangIPaddr = function(address) {
//     defangIpAdd =''
//     for (i of address){
//         if (i === '.')
//             defangIpAdd += '[.]'
//         else{
//             defangIpAdd += i
//         }
//     }
//     return defangIpAdd
// };

// console.log(defangIPaddr(address = "1.1.1.1"))



// function reverseString(s : string[]): string[] {

//     let left = 0;
//     let right = s.length-1 
//     for(let i = 0;i<s.length/2;i++){
//         let temp = s[left]
//         s[left] = s[right]
//         s[right] = temp
//         left ++
//         right --

//     }
//     return s
    
    
// };

// let s = ['h','e','l','l','o']
// console.log(reverseString(s))


function twoSum(nums: number[], target: number): number[] {
    let result
    for(let i =0;i<nums.length;i++){
        for(let j =0;j<nums.length;j++){
            if(nums[i]+nums[j] == target){
                result = [i,j]
                break
            }
        }

        

    }
    return result
};

let nums = [2,7,11,15]
let target = 18
console.log(twoSum(nums,target))