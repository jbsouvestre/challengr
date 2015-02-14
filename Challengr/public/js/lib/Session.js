import {Model} from 'backbone';
import utils from 'utils';

class Session extends Model {
    constructor(){
        super(...arguments);
    }

    url(){
        return utils.api.url('accounts/this');
    }
}


export default new Session();