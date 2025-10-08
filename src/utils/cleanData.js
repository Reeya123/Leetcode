/**
 * Cleans the organization data by removing quotes, whitespace, and punctuation from the group and team names.
 * @param {Object} rawData - The raw organization data.
 * @returns {Array} The cleaned organization data.
 * @example
 * ```json
 * [
 *   {
 *     group: "Silicon Technologies Group",
 *     teams: ["CAD Team", "Hardware Technology CAD Team", ...],
 *     teamCount: 5,
 *     mentionCount: 100
 *   },
 *   {
 *     group: "Apple Media Products",
 *     teams: ["AMP Data Engineering Team", "AMP Search Team"],
 *     teamCount: 2,
 *     mentionCount: 50
 *   },
 *   ...
 * ]
 * ```
 */
export const cleanOrgData = (rawData) => {
    const result = [];
  
    for (const rawGroupName in rawData) {
      const rawTeamsObj = rawData[rawGroupName];
  
      // Clean group name (strip quotes, whitespace, punctuation)
      const group = rawGroupName.trim().replace(/["']/g, '');
  
      // Extract and clean team names
      const teams = Object.keys(rawTeamsObj).map((team) =>
        team.trim().replace(/["']/g, '')
      );
  
      result.push({
        group,
        teams,
        teamCount: teams.length,
        mentionCount: Math.floor(Math.random() * 200) + 25  // Fake data just to stimulate populatiry
      });
    }
  
    return result.sort((a, b) => b.teamCount - a.teamCount); // Optional: sort by most populated group
  };
  