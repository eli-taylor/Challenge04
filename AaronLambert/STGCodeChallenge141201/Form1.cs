using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace STGCodeChallenge141201
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnCalculate_Click(object sender, EventArgs e)
        {
            string Input = txtInput.Text;
            int Total = 0;
            int LetterCount = 0;
            int indx = 0;
            char c;

            while (indx < Input.Length)
            {
                c = Input[indx];
                if (Char.IsLetter(c))
                {
                    LetterCount++;
                    indx++;
                }
                else if (Char.IsDigit(c) || c == '-')
                {
                    int start, len;

                    // We have come across some kind of number
                    // Find the end and convert it to an int
                    start = indx;
                    len = 1;
                    indx++;
                    while (indx < Input.Length && Char.IsDigit(Input, indx))
                    {
                        indx++;
                        len++;
                    }
                    string num = Input.Substring(start, len);
                    int i;
                    if (!int.TryParse(num, out i))
                    {
                        MessageBox.Show("Invalid input was detected");
                        return;
                    }
                    else
                    {
                        Total += i;
                    }
                }
                else
                {
                    // Not a letter or number, just skip it
                    indx++;
                }
            }

            int Result;
            if (LetterCount > 0)
            {
                Result = (int)Math.Round((decimal)Total / LetterCount, MidpointRounding.AwayFromZero);
            }
            else
            {
                Result = 0;
            }
            MessageBox.Show(string.Format("The answer is {0}.", Result.ToString()));
        }
    }
}
