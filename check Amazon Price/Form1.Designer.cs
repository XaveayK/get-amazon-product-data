namespace check_Amazon_Price
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.textTitle = new System.Windows.Forms.TextBox();
            this.maskedTextURI = new System.Windows.Forms.MaskedTextBox();
            this.listView1 = new System.Windows.Forms.ListView();
            this.SuspendLayout();
            // 
            // textTitle
            // 
            this.textTitle.Location = new System.Drawing.Point(12, 12);
            this.textTitle.Name = "textTitle";
            this.textTitle.Size = new System.Drawing.Size(101, 20);
            this.textTitle.TabIndex = 4;
            // 
            // maskedTextURI
            // 
            this.maskedTextURI.Location = new System.Drawing.Point(12, 38);
            this.maskedTextURI.Name = "maskedTextURI";
            this.maskedTextURI.Size = new System.Drawing.Size(101, 20);
            this.maskedTextURI.TabIndex = 5;
            // 
            // listView1
            // 
            this.listView1.HideSelection = false;
            this.listView1.Location = new System.Drawing.Point(193, 52);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(419, 341);
            this.listView1.TabIndex = 6;
            this.listView1.UseCompatibleStateImageBehavior = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.maskedTextURI);
            this.Controls.Add(this.textTitle);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textTitle;
        private System.Windows.Forms.MaskedTextBox maskedTextURI;
        private System.Windows.Forms.ListView listView1;
    }
}

