import { Model } from 'backbone';
import utils from 'utils';


class Game extends Model {
    constructor(){
        super(...arguments);
    }

    url(){
        return utils.api.url('game');
    }

    defaults(){
        return {
            
        }       
    }
}

export default Game;