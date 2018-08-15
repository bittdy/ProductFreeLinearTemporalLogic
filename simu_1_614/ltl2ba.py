#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import abspath, dirname, join
from subprocess import check_output
from codecs import getdecoder
from argparse import ArgumentParser
from promela import Parser

def run_ltl2ba(formula):
    script_dir = dirname(abspath(__file__))
    ltl2ba = join(script_dir, "ltl2ba")
    raw_output = check_output([ltl2ba, "-f", "%s" % formula])
    #raw_output = b"never { /* G(goods->Xdepot)&&G(depot->Xgoods)&&(G(!b)&&G(!door||open)) */accept_init : /* init */if:: (!goods && !depot && !b && !door) || (!goods && !depot && !b && open) -> goto accept_init	:: (!goods && !b && !door) || (!goods && !b && open) -> goto accept_S2	:: (!depot && !b && !door) || (!depot && !b && open) -> goto accept_S3	:: (!b && !door) || (!b && open) -> goto accept_S4	fi;accept_S2 :    /* 1 */	if	:: (goods && !depot && !b && !door) || (goods && !depot && !b && open) -> goto accept_S3	:: (goods && !b && !door) || (goods && !b && open) -> goto accept_S4	fi;accept_S3 :    /* 2 */	if	:: (!goods && depot && !b && !door) || (!goods && depot && !b && open) -> goto accept_S2	:: (depot && !b && !door) || (depot && !b && open) -> goto accept_S4	fi;accept_S4 :    /* 3 */	if	:: (goods && depot && !b && !door) || (goods && depot && !b && open) -> goto accept_S4	fi;}"
    ascii_decoder = getdecoder("ascii")
    (output, _) = ascii_decoder(raw_output)
    #print 'Output from ltl2ba'
    #print output
    #output = "never { /* G(goods->Xdepot)&&G(depot->Xgoods)&&(G(!b)&&G(!door||open)) */    accept_init :    /* init */    if	:: (!goods && !depot && !b && !door) || (!goods && !depot && !b && open) -> goto accept_init	:: (!goods && !b && !door) || (!goods && !b && open) -> goto accept_S2	:: (!depot && !b && !door) || (!depot && !b && open) -> goto accept_S3	:: (!b && !door) || (!b && open) -> goto accept_S4	fi;accept_S2 :    /* 1 */	if	:: (goods && !depot && !b && !door) || (goods && !depot && !b && open) -> goto accept_S3	:: (goods && !b && !door) || (goods && !b && open) -> goto accept_S4	fi;accept_S3 :    /* 2 */	if	:: (!goods && depot && !b && !door) || (!goods && depot && !b && open) -> goto accept_S2	:: (depot && !b && !door) || (depot && !b && open) -> goto accept_S4	fi;accept_S4 :    /* 3 */	if	:: (goods && depot && !b && !door) || (goods && depot && !b && open) -> goto accept_S4	fi;}"
    return output

def parse_ltl(formula):
    ltl2ba_output = run_ltl2ba(formula)
    parser = Parser(ltl2ba_output)
    edges = parser.parse()
    return edges

if __name__ == "__main__":
    argparser = ArgumentParser(description="Call the ltl2ba program and parse the output")
    argparser.add_argument('LTL')
    args = argparser.parse_args()
    ltl2ba_output = run_ltl2ba(args.LTL)
    parser = Parser(ltl2ba_output)
    transitions = parser.parse()
    print(transitions)
