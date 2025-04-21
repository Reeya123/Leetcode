/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    let light = 0;
    let heavy = people.length - 1;

    people.sort((a, b) => a - b);  // Sort numerically

    let count = 0;

    while (light <= heavy) {
        if (people[light] + people[heavy] <= limit) {
            light++;
        }
        heavy--;
        count++;
    }

    return count;
};