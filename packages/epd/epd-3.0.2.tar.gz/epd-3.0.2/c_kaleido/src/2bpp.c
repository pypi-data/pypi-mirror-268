#include <stdint.h>
#include <string.h>
// FIXME make it workable for all different display sizes (not only 13.3 1600x1200)

#define W 1600
#define H 1200
#define STEP 3

static uint8_t NO_RED[3] = {2,1,4};
static uint8_t NO_GREEN[3] = {1,4,2};
static uint8_t NO_BLUE[3] = {4,2,1};

static uint8_t epd_header[16] = {0x45, 0x50, 0x44, 0x32, 0x40, 0x06, 0xB0, 0x04, 0x04, 0x80, 0xA9, 0x03, 0x00, 0x00, 0x00, 0x00};

volatile static uint8_t color[2];

static uint8_t calc_color(uint8_t a, uint32_t avg_blue, uint32_t avg_green, uint32_t avg_red)
{
    color[0]=0;
    color[1]=0;

    if(avg_blue<64)
    {
        color[0] |= NO_BLUE[a];
        color[1] |= NO_BLUE[a];
    }
    else if(avg_blue<128)
    {
        color[1] |= NO_BLUE[a];
    }
    else if(avg_blue<192)
    {
        color[0] |= NO_BLUE[a];
    }

    if(avg_green<64)
    {
        color[0] |= NO_GREEN[a];
        color[1] |= NO_GREEN[a];
    }
    else if(avg_green<128)
    {
        color[1] |= NO_GREEN[a];
    }
    else if(avg_green<192)
    {
        color[0] |= NO_GREEN[a];
    }

    if(avg_red<64)
    {
        color[0] |= NO_RED[a];
        color[1] |= NO_RED[a];
    }
    else if(avg_red<128)
    {
        color[1] |= NO_RED[a];
    }
    else if(avg_red<192)
    {
        color[0] |= NO_RED[a];
    }

}


void kaleido_convert_2bpp(uint8_t* in, uint8_t* out, uint16_t width, uint16_t height)
{
    uint8_t (*outs)[2][H][(W>>3)];
    outs = out+32;

    memcpy(out,epd_header,16);
    memcpy(out+16,epd_header,16);

    for (int y = 0; y < H; y+=STEP) // loop for rows
    {
        for (int x = 0; x < W; x+=STEP) // loop for columns
        {
            for(uint8_t a=0; a<STEP; a++) // loop for colors
            {
                uint32_t z = x>>3;
                int8_t q = 5 - (x%8);
                uint32_t avg_blue=0;
                uint32_t avg_green=0;
                uint32_t avg_red=0;

                avg_red = in[((y+a)*W*3)+x*3] + in[((y+a)*W*3)+x*3+3] + in[((y+a)*W*3)+x*3+6];
                avg_green = in[((y+a)*W*3)+x*3+1] + in[((y+a)*W*3)+x*3+4] + in[((y+a)*W*3)+x*3+7];
                avg_blue = in[((y+a)*W*3)+x*3+2] + in[((y+a)*W*3)+x*3+5] + in[((y+a)*W*3)+x*3+8];
                
                avg_blue /=3;
                avg_green /=3;
                avg_red /=3;
                
                calc_color(a, avg_blue, avg_green, avg_red);

                if(q == -1)
                {
                    (*outs)[0][y+a][z] |= color[0] >> 1;
                    (*outs)[1][y+a][z] |= color[1] >> 1;
                    if(z < (W>>3)-1) // if not last byte prepare next one     
                    {
                        (*outs)[0][y+a][z+1] = color[0] << 7;
                        (*outs)[1][y+a][z+1] = color[1] << 7;
                    } 
                }
                else if(q == -2)
                {
                    (*outs)[0][y+a][z] |= color[0] >> 2;
                    (*outs)[1][y+a][z] |= color[1] >> 2;
                    if(z < (W>>3)-1) // if not last byte prepare next one     
                    {
                        (*outs)[0][y+a][z+1] = color[0] << 6;
                        (*outs)[1][y+a][z+1] = color[1] << 6;
                    } 
                }
                else
                {
                    (*outs)[0][y+a][z] |= color[0] << q;
                    (*outs)[1][y+a][z] |= color[1] << q;
                }

            }
        }
    }
}