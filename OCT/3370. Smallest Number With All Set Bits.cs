public class Solution {
    public int SmallestNumber(int n) {
        // Find the position of the most significant bit
        // 31 - LeadingZeroCount gives us the MSB position
        int msb = 31 - System.Numerics.BitOperations.LeadingZeroCount((uint)n);
        
        // Create a number with (msb+1) bits all set to 1
        int result = (1 << (msb + 1)) - 1;
        
        return result;
    }
}
