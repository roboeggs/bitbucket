#include <iostream>
#include <bitset>

bool IsCorrectMask(const std::string& bit_mask) {
    if (bit_mask.length() != 32) {
        std::cout << "Error: Input string must be 32 bits long." << std::endl;
        return false;
    }

    for (char c : bit_mask) {
        if (c != '0' && c != '1') {
            std::cout << "Error: Input string must contain only '0' or '1'." << std::endl;
            return false;
        }
    }

    std::bitset<32> bit_set(bit_mask);
    bool has_seen_zero = false;
    for (int i = 31; i >= 0; --i) {
        if (bit_set[i]) {
            if (has_seen_zero) {
                return false;
            }
        }
        else {
            has_seen_zero = true;
        }
    }
    return true;
}

int main() {
    // Тестирование функции IsCorrectMask
    std::cout << "Testing IsCorrectMask function...\n";

    // Правильные маски
    std::cout << "Test case 1: " << (IsCorrectMask("11110000000000000000000000000000") ? "Passed" : "Failed") << "\n";
    std::cout << "Test case 2: " << (IsCorrectMask("11111000000000000000000000000000") ? "Passed" : "Failed") << "\n";
    std::cout << "Test case 3: " << (IsCorrectMask("11111111111100000000000000000000") ? "Passed" : "Failed") << "\n";
    std::cout << "Test case 7: " << (IsCorrectMask("00000000000000000000000000000000") ? "Passed" : "Failed") << "\n";

    // Неправильные маски
    std::cout << "Test case 4: " << (!IsCorrectMask("10110000000000000000000000001000") ? "Passed" : "Failed") << "\n";
    std::cout << "Test case 5: " << (!IsCorrectMask("01111100000000000000001000000001") ? "Passed" : "Failed") << "\n";
    std::cout << "Test case 6: " << (!IsCorrectMask("00000000000000000000000000000001") ? "Passed" : "Failed") << "\n";
    std::cout << "Test case 7: " << (!IsCorrectMask("00000000000000000000000 00000000") ? "Passed" : "Failed") << "\n";
    std::cout << "Test case 8: " << (!IsCorrectMask("0000000003000000000000000000000") ? "Passed" : "Failed") << "\n";
    std::cout << "Test case 8: " << (!IsCorrectMask("0000000003000000000000000000000s") ? "Passed" : "Failed") << "\n";

    return 0;
}