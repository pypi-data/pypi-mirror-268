# include <stdint.h>
# include <stdio.h>


// This implements the tausworthe generator found at this location:  https://www.eevblog.com/forum/fpga/a-uniform-pseudo-random-number-generator/
// It has a 96-bit seed, using s0, s1 and s2. All three should be initialised non-zero. The base code produces 32-bit random numbers however
// to get 16-bit random numbers the uppermost 16 bits are taken.

uint16_t tausworthe(void) {
    static uint32_t s0=0xFFFFFFFFU, s1=0xFFFFFFFFU, s2=0xFFFFFFFFU;

    s0 = ((s0 & 0xFFFFFFFE) << 12) ^ (((s0 <<13)  ^  s0) >> 19);
    s1 = ((s1 & 0xFFFFFFF8) <<  4) ^ (((s1 << 2)  ^  s1) >> 25);
    s2 = ((s2 & 0xFFFFFFF0) << 17) ^ (((s2 << 3)  ^  s2) >> 11);
    uint32_t result = s0 ^ s1 ^ s2;
    return result >> 16;
}

int main() {
    uint32_t result = tausworthe();
    printf("Tausworthe result: %u\n", result);
    result = tausworthe();
    printf("Tausworthe result: %u\n", result);
}
