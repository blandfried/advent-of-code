#!/usr/bin/perl
use strict;
use warnings;

use Path::Tiny;
use autodie;    # die if problem reading or writing a file
use List::Util qw(sum);

my $dir = path("./");    # /tmp

my $file = $dir->child("day1Input.txt");

# Read in the entire contents of a file
my $content = $file->slurp_utf8();

# openr_utf8() returns an IO::File object to read from
# with a UTF-8 decoding layer
my $file_handle = $file->openr_utf8();

my @left_list  = ();
my @right_list = ();

# Read in line at a time
while ( my $line = $file_handle->getline() ) {
    my @spl = split( /\s+/, $line );
    push @left_list,  $spl[0];
    push @right_list, $spl[1];

}

my @sorted_left_list = sort { $a <=> $b } @left_list;

my @sorted_right_list = sort { $a <=> $b } @right_list;

my @distances_list = ();
foreach my $i ( 0 .. $#sorted_left_list ) {
    my $distance = $sorted_left_list[$i] - $sorted_right_list[$i];
    push @distances_list, abs($distance);
}

print sum(@distances_list);
