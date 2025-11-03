// Check if a number is palindrome or not
#include <stdio.h>
int main() {
    int n, temp, rev = 0, r;
    printf("Enter number: ");
    scanf("%d", &n);
    temp = n;
    while (n > 0) {
        r = n % 10;
        rev = rev * 10 + r;
        n = n / 10;
    }
    if (temp == rev) printf("%d is a Palindrome", temp);
    else printf("%d is a Not Palindrome", temp);
    return 0;
}


// Print Fibonacci series up to n terms
#include <stdio.h>
int main() {
    int n, a = 0, b = 1, c, i;
    printf("Enter n terms: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++) {
        printf("%d ", a);
        c = a + b;
        a = b;
        b = c;
    }
    return 0;
}


// Check if a number is Armstrong or not
#include <stdio.h>
#include <math.h>

int main() {
    int n, temp, r, sum = 0;
    printf("Enter number: ");
    scanf("%d", &n);

    temp = n;
    int digits = log10(n) + 1;  // simpler way to get digits

    while (temp > 0) {
        r = temp % 10;
        sum += pow(r, digits);
        temp /= 10;
    }

    (sum == n) ? printf("Armstrong") : printf("Not Armstrong");
    return 0;
}


// Check if a string is palindrome or not
#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    printf("Enter string: ");
    scanf("%s", s);

    int len = strlen(s);
    int i;
    int isPalindrome = 1;

    for (i = 0; i < len/2; i++) {
        if (s[i] != s[len - 1 - i]) {
            isPalindrome = 0;
            break;
        }
    }

    if (isPalindrome)
        printf("Palindrome");
    else
        printf("Not Palindrome");

    return 0;
}


// Calculate sum of digits of a number
#include <stdio.h>
int main() {
    int n, sum = 0, r;
    printf("Enter number: ");
    scanf("%d", &n);
    while (n > 0) {
        r = n % 10;
        sum += r;
        n /= 10;
    }
    printf("Sum = %d", sum);
    return 0;
}


// Add two matrices
#include <stdio.h>
int main() {
    int a[10][10], b[10][10], sum[10][10];
    int r, c, i, j;

    printf("Enter rows and cols: ");
    scanf("%d %d", &r, &c);

    printf("Enter matrix A:\n");
    for(i=0;i<r;i++)
        for(j=0;j<c;j++)
            scanf("%d",&a[i][j]);

    printf("Enter matrix B:\n");
    for(i=0;i<r;i++)
        for(j=0;j<c;j++)
            scanf("%d",&b[i][j]);

    for(i=0;i<r;i++)
        for(j=0;j<c;j++)
            sum[i][j] = a[i][j] + b[i][j];

    printf("Sum matrix:\n");
    for(i=0;i<r;i++){
        for(j=0;j<c;j++)
            printf("%d ", sum[i][j]);
        printf("\n");
    }
    return 0;
}


// Read and print a paragraph
#include <stdio.h>

int main() {
    char paragraph[500]; // Buffer to store the input

    printf("Enter a paragraph:\n");
    
    // Read a line of text into the 'paragraph' buffer
    fgets(paragraph, sizeof(paragraph), stdin);
    
    printf("\nInput received: %s\n", paragraph);

    return 0;
}


// Print a right-angled triangle pattern of stars
#include <stdio.h>
int main() {
    int n,i,j;
    scanf("%d",&n);

    for(i=1;i<=n;i++){
        for(j=1;j<=i;j++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
// *
// **
// ***
// ****
// *****



// Print an inverted right-angled triangle pattern of stars
#include <stdio.h>
int main() {
    int n,i,j;
    scanf("%d",&n);

    for(i=n;i>=1;i--){
        for(j=1;j<=i;j++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
// *****
// ****
// ***
// **
// *



// Print a pyramid pattern of stars
#include <stdio.h>
int main() {
    int n,i,j;
    scanf("%d",&n);

    for(i=1;i<=n;i++){
        // print spaces
        for(j=1;j<=n-i;j++){
            printf(" ");
        }
        // print stars
        for(j=1;j<=2*i-1;j++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
//     *
//    ***
//   *****
//  *******
// *********



// Print a right-aligned triangle pattern of stars
#include <stdio.h>
int main() {
    int n,i,j;
    scanf("%d",&n);

    for(i=1;i<=n;i++){
        for(j=1;j<=n-i;j++){
            printf(" ");   // spaces first
        }
        for(j=1;j<=i;j++){
            printf("*");   // then stars
        }
        printf("\n");
    }
    return 0;
}
//     *
//    **
//   ***
//  ****
// *****
