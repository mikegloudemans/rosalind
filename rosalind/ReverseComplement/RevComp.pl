use strict;
use warnings;

my $filename = "DNA.txt";

# open the file
open(FILE, $filename) || die("cannot open file $filename: $!");

# Loop over each line
while (my $line = <FILE>)
{
	my $str = reverse("$line");
	$str =~ tr/ACGT/TGCA/;
	print $str;
}
