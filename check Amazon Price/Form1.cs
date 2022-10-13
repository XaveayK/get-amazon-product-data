using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace check_Amazon_Price
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            maskedTextURI.KeyDown += new KeyEventHandler(enterKey);
        }
        void enterKey(object sender, KeyEventArgs e) 
        {
            if (e.KeyCode == Keys.Enter) 
            {
                // Ensures it only moves forward if both title and URI are present, doesn't validate authenticity.
                // TODO: Add URI authenticity check
                // TODO: Create program that gets the title for the user so the user only needs to enter URI
                if (String.IsNullOrEmpty(maskedTextURI.Text)) { return; } 
                else if (String.IsNullOrEmpty(textTitle.Text)) { return; }

                var p = new Process
                {
                    StartInfo =
                    {
                        FileName = "python",
                        WorkingDirectory = @"E:\code\get-amazon-product-data",
                        Arguments = $"main.py -a {textTitle.Text} {maskedTextURI.Text}"
                    }
                }.Start();
            }
        }


    }


}
