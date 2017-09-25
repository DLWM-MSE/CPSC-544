from PrintControl.ModPrint import ModPrint

def main():
    
    print(ModPrint.bold("Bold"))
    print(ModPrint.red("Red"))

    ModPrint.print_bold("BOLD")
    ModPrint.print_red("RED")

    bblarr = [1,2,3,4]
    loc = (0,3)
    ModPrint.print_bold_bbl_arr(bblarr, loc)
    ModPrint.print_yllw_bbl_arr(bblarr, loc)
if __name__ == "__main__": main()