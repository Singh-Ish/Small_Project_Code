using System;
using System.Collections.Generic;
using System.Text;

namespace ClassLibrary
{
    public class School
    {
        public School()
        {
            Name = "Untitled School";
            phonenumber = "555-1234";

        }

        public string Name { get; set; }
        public string address { get; set; }
        public string city { get; set; }

        public string state { get; set; }
        public string zip { get; set; }
        public string phonenumber { get; set; }

        private string _twitteraddress;

        public string TwitterAddress
        {
            //make sure the twitter address startwith !
            get { return _twitteraddress; }
            set
            {
                if (value.StartsWith("@"))
                {
                    _twitteraddress = value;
                }
                else
                {
                    throw new Exception("The twitter expression must begin with @");
                }
            }
        }
      


    }
}
