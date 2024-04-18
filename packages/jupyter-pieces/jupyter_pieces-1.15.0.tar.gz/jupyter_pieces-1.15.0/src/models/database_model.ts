import { Directive } from 'copilot/dist/types/Directive';
import { returnedSnippet } from './typedefs';

export default interface PiecesDB {
  assets: returnedSnippet[];
  selectedModel: string;
  directives: Directive[];
}
