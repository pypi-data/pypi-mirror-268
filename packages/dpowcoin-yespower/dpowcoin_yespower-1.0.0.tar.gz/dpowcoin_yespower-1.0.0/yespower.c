#include "yespower.h"
#include "sysendian.h"
/* 
 * yespower_1.0.1 for dpowcoin
 */
int yespower_hash(const char *input, char *output)
{
    yespower_params_t params = {YESPOWER_1_0, 2048, 8, "One POW? Why not two? 17/04/2024", 32};
    return yespower_tls(input, 80, &params, (yespower_binary_t *) output);
}
