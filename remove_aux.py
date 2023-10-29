import os
import glob
import logging

to_remove = ['aux', 'gz', 'fls', 'log', 'out', 
             'toc', 'blg', 'fdb_latexmk', 
            'bcf', 'xml', 'dvi', 'pdf', 'bbl']

logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == "__main__":
    if 'tex' in to_remove:
        raise Exception("\nDo not remove .tex\n")
    else:    
        for item in to_remove:            
            aux_list = glob.glob(f"**/*.{item}", recursive = True)
            for dir in aux_list:    
                try:
                    os.remove(dir)
                    logging.info(f"Removed {dir}")
                except:
                    logging.warning(f"Failed to remove {dir}")
        logging.info("Done")