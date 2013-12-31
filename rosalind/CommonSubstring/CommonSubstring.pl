use strict;
use warnings;

# Courtesy of somacon.com:
sub trim($)
{
	my $string = shift;
	$string =~ s/^\s+//;
	$string =~ s/\s+$//;
	return $string;
}

my $filename = "Seqs.txt";

# open the file
open(FILE, $filename) || die("cannot open file $filename: $!");

my @seqs = ();
my $min_length = 1000000;
while (my $line = <FILE>)
{
	$line = trim($line);
	push @seqs, $line;
	if (length($line) < $min_length)
	{
		$min_length = length($line);
	}
}

for (my $k = $min_length; $k > 0; $k -= 1)
{
	my $answer_found = 0;
	foreach my $i (0..(length($seqs[0])-$k))
	{
		my $sub = substr($seqs[0], $i, $k);
		my $failed = 0;
		foreach my $j (1..(scalar(@seqs)-1))
		{
			if (!($seqs[$j] =~ m/($sub)/))
			{
				$failed = 1;
				last;
			}
		}
		if ($failed)
		{
			next;
		}
		else
		{
			print $sub;
			exit;
		}
	}
		
}




